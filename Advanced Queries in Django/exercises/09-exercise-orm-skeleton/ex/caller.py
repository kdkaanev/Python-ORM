import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries
# Create instances of RealEstateListing with locations
from main_app.models import RealEstateListing, VideoGame, Invoice, BillingInfo

# Create BillingInfo instances with real addresses

# Get invoices starting with a specific prefix
invoices_with_prefix = Invoice.get_invoices_with_prefix("INV")
for invoice in invoices_with_prefix:
    print(f"Invoice Number with prefix INV: {invoice.invoice_number}")

# Get invoices sorted by invoice number
invoices_sorted = Invoice.get_invoices_sorted_by_number()
for invoice in invoices_sorted:
    print(f"Invoice Number: {invoice.invoice_number}")

# Get an invoice by a specific invoice number along with its related billing info
invoice = Invoice.get_invoice_with_billing_info("INV002")
print(f"Invoice Number: {invoice.invoice_number}")
print(f"Billing Info: {invoice.billing_info.address}")
