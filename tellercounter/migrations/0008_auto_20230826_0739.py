# Generated by Django 3.2 on 2023-08-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellercounter', '0007_delete_tellercounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='chequecontributor',
            name='bank_cheque',
            field=models.CharField(blank=True, choices=[('Abhyudaya Co-op Bank', 'Abhyudaya Co-op Bank'), ('Allahabad Bank', 'Allahabad Bank'), ('Andhra Bank', 'Andhra Bank'), ('Apna Sahakari Bank', 'Apna Sahakari Bank'), ('Axis Bank', 'Axis Bank'), ('Bandhan Bank', 'Bandhan Bank'), ('Bank Of Baroda', 'Bank Of Baroda'), ('Bank of India', 'Bank of India'), ('Bank of Maharashtra', 'Bank of Maharashtra'), ('Bhartiya Mahila Bank', 'Bhartiya Mahila Bank'), ('Canara Bank', 'Canara Bank'), ('Central Bank of India', 'Central Bank of India'), ('Citi bank', 'Citi bank'), ('Corporation Bank', 'Corporation Bank'), ('DCB Bank', 'DCB Bank'), ('Federal Bank', 'Federal Bank'), ('Grameen Bank', 'Grameen Bank'), ('Gujarat State Co-op Bank', 'Gujarat State Co-op Bank'), ('Hasti Co-op Bank', 'Hasti Co-op Bank'), ('HDFC Bank', 'HDFC Bank'), ('ICICI Bank', 'ICICI Bank'), ('IDBI Bank', 'IDBI Bank'), ('IDFC Bank', 'IDFC Bank'), ('Indian Bank', 'Indian Bank'), ('Indian Overseas Bank', 'Indian Overseas Bank'), ('IndusInd Bank', 'IndusInd Bank'), ('ING Vysya Bank', 'ING Vysya Bank'), ('Janata Sahakari Bank', 'Janata Sahakari Bank'), ('Karnataka Bank', 'Karnataka Bank'), ('Karur Vysya Bank', 'Karur Vysya Bank'), ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'), ('Mehsana Urban Co-op Bank', 'Mehsana Urban Co-op Bank'), ('Nainital Bank', 'Nainital Bank'), ('NKGSB Co-op Bank', 'NKGSB Co-op Bank'), ('Oriental Bank of Commerce', 'Oriental Bank of Commerce'), ('Others', 'Others'), ('Post Office', 'Post Office'), ('Punjab & Maharashtra Co-op Bank', 'Punjab & Maharashtra Co-op Bank'), ('Punjab National Bank', 'Punjab National Bank'), ('Punjab & Sind Bank', 'Punjab & Sind Bank'), ('RBL Bank', 'RBL Bank'), ('Saraswat Bank', 'Saraswat Bank'), ('State Bank of Bikaner & Jaipur', 'State Bank of Bikaner & Jaipur'), ('State Bank of Hyderabad', 'State Bank of Hyderabad'), ('State Bank Of India', 'State Bank Of India'), ('State Bank of Mysore', 'State Bank of Mysore'), ('State Bank of Patiala', 'State Bank of Patiala'), ('State Bank of Travancore', 'State Bank of Travancore'), ('Syndicate Bank', 'Syndicate Bank'), ('Tamilnad Mercantile Bank', 'Tamilnad Mercantile Bank'), ('The South Indian Bank', 'The South Indian Bank'), ('UCO Bank', 'UCO Bank'), ('Union Bank of India', 'Union Bank of India'), ('United Bank of India', 'United Bank of India'), ('Vijaya Bank', 'Vijaya Bank'), ('Yes Bank', 'Yes Bank')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='draftcontributor',
            name='bank_cheque',
            field=models.CharField(blank=True, choices=[('Abhyudaya Co-op Bank', 'Abhyudaya Co-op Bank'), ('Allahabad Bank', 'Allahabad Bank'), ('Andhra Bank', 'Andhra Bank'), ('Apna Sahakari Bank', 'Apna Sahakari Bank'), ('Axis Bank', 'Axis Bank'), ('Bandhan Bank', 'Bandhan Bank'), ('Bank Of Baroda', 'Bank Of Baroda'), ('Bank of India', 'Bank of India'), ('Bank of Maharashtra', 'Bank of Maharashtra'), ('Bhartiya Mahila Bank', 'Bhartiya Mahila Bank'), ('Canara Bank', 'Canara Bank'), ('Central Bank of India', 'Central Bank of India'), ('Citi bank', 'Citi bank'), ('Corporation Bank', 'Corporation Bank'), ('DCB Bank', 'DCB Bank'), ('Federal Bank', 'Federal Bank'), ('Grameen Bank', 'Grameen Bank'), ('Gujarat State Co-op Bank', 'Gujarat State Co-op Bank'), ('Hasti Co-op Bank', 'Hasti Co-op Bank'), ('HDFC Bank', 'HDFC Bank'), ('ICICI Bank', 'ICICI Bank'), ('IDBI Bank', 'IDBI Bank'), ('IDFC Bank', 'IDFC Bank'), ('Indian Bank', 'Indian Bank'), ('Indian Overseas Bank', 'Indian Overseas Bank'), ('IndusInd Bank', 'IndusInd Bank'), ('ING Vysya Bank', 'ING Vysya Bank'), ('Janata Sahakari Bank', 'Janata Sahakari Bank'), ('Karnataka Bank', 'Karnataka Bank'), ('Karur Vysya Bank', 'Karur Vysya Bank'), ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'), ('Mehsana Urban Co-op Bank', 'Mehsana Urban Co-op Bank'), ('Nainital Bank', 'Nainital Bank'), ('NKGSB Co-op Bank', 'NKGSB Co-op Bank'), ('Oriental Bank of Commerce', 'Oriental Bank of Commerce'), ('Others', 'Others'), ('Post Office', 'Post Office'), ('Punjab & Maharashtra Co-op Bank', 'Punjab & Maharashtra Co-op Bank'), ('Punjab National Bank', 'Punjab National Bank'), ('Punjab & Sind Bank', 'Punjab & Sind Bank'), ('RBL Bank', 'RBL Bank'), ('Saraswat Bank', 'Saraswat Bank'), ('State Bank of Bikaner & Jaipur', 'State Bank of Bikaner & Jaipur'), ('State Bank of Hyderabad', 'State Bank of Hyderabad'), ('State Bank Of India', 'State Bank Of India'), ('State Bank of Mysore', 'State Bank of Mysore'), ('State Bank of Patiala', 'State Bank of Patiala'), ('State Bank of Travancore', 'State Bank of Travancore'), ('Syndicate Bank', 'Syndicate Bank'), ('Tamilnad Mercantile Bank', 'Tamilnad Mercantile Bank'), ('The South Indian Bank', 'The South Indian Bank'), ('UCO Bank', 'UCO Bank'), ('Union Bank of India', 'Union Bank of India'), ('United Bank of India', 'United Bank of India'), ('Vijaya Bank', 'Vijaya Bank'), ('Yes Bank', 'Yes Bank')], max_length=50, null=True),
        ),
    ]