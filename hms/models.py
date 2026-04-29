from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='patient_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)
    specialist = models.CharField(max_length=100, blank=True, null=True)
    hospital_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    consultancy_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    # NEW: Doctor next 7 days availability
    available_from_time = models.TimeField(blank=True, null=True)
    available_to_time = models.TimeField(blank=True, null=True)
    availability_note = models.CharField(max_length=255, blank=True, null=True)
    availability_updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=150)
    contact = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='receptionist_profiles/', blank=True, null=True)

    def __str__(self):
        return self.organization_name


from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject or 'No Subject'}"


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending Receptionist', 'Pending Receptionist'),
        ('Booked', 'Booked'),
        ('Arrived', 'Arrived'),
        ('Waiting', 'Waiting'),
        ('In Consultation', 'In Consultation'),
        ('Completed', 'Completed'),
        ('Missed', 'Missed'),
        ('Cancelled by Patient', 'Cancelled by Patient'),
        ('Cancelled by Doctor', 'Cancelled by Doctor'),
    )

    MODE_CHOICES = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    )

    CATEGORY_CHOICES = (
        ('General Checkup', 'General Checkup'),
        ('Fever / Cold', 'Fever / Cold'),
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Neurology', 'Neurology'),
        ('Orthopedic', 'Orthopedic'),
        ('Gynecology', 'Gynecology'),
        ('ENT', 'ENT'),
        ('Other', 'Other'),
    )

    URGENCY_CHOICES = (
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
        ('Emergency', 'Emergency'),
    )

    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('Cash', 'Cash'),
            ('Bkash', 'Bkash'),
        ],
        blank=True,
        null=True
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()

    # UPDATED: patient will not choose time. Receptionist will assign later.
    appointment_time = models.TimeField(blank=True, null=True)

    consultancy_fee = models.DecimalField(max_digits=10, decimal_places=2)
    appointment_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='Offline')
    problem_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='General Checkup')
    urgency_level = models.CharField(max_length=20, choices=URGENCY_CHOICES, default='Normal')
    symptoms = models.TextField(blank=True, null=True)
    meeting_link = models.URLField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_number = models.CharField(max_length=20, blank=True, null=True)

    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Paid', 'Paid'),
            ('Unpaid', 'Unpaid'),
        ],
        default='Unpaid'
    )

    visit_note = models.CharField(max_length=255, blank=True, null=True)

    # NEW: Receptionist assigned message/time info
    receptionist_message = models.TextField(blank=True, null=True)
    receptionist_assigned_at = models.DateTimeField(blank=True, null=True)
    patient_message_seen = models.BooleanField(default=False)
    patient_message_seen_at = models.DateTimeField(blank=True, null=True)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending Receptionist'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} -> {self.doctor}"
    
class Prescription(models.Model):
    appointment = models.OneToOneField('Appointment', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    symptoms_snapshot = models.TextField(blank=True, null=True)
    prescription_text = models.TextField()
    test = models.TextField(blank=True, null=True)
    advice = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription - {self.patient.first_name} - {self.doctor.name}"

class DoctorPatientBookmark(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'patient')

    def __str__(self):
        return f"{self.doctor.name} -> {self.patient.first_name} {self.patient.last_name}"

from django.db import models
from django.utils import timezone


class ReportShow(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processed', 'Processed'),
    )

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='report_requests')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='report_requests')
    previous_appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='followup_reports')
    previous_prescription = models.FileField(upload_to='report_show/prescriptions/', blank=True, null=True)
    report_note = models.TextField(blank=True, null=True)
    submitted_date = models.DateField(default=timezone.localdate)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.patient.first_name} -> Dr. {self.doctor.name} ({self.status})"


class ReportShowFile(models.Model):
    report_show = models.ForeignKey(ReportShow, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='report_show/files/')

    def __str__(self):
        return f"Report File #{self.id} - {self.report_show.patient.first_name}"


class MedicalTest(models.Model):
    name = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price}"


class TestReport(models.Model):
    patient_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    receptionist = models.ForeignKey('Receptionist', on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=150)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.contact_number}"


class TestReportItem(models.Model):
    report = models.ForeignKey(TestReport, on_delete=models.CASCADE, related_name='items')
    medical_test = models.ForeignKey(MedicalTest, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=150)
    test_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.report.patient_name} - {self.test_name}"