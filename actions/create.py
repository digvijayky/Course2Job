from sparkpost import SparkPost

sp = SparkPost('3b96fba1be67bfc6addbfad1b5ddb35bda21af68')

response = sp.templates.create(
    id='TEST_ID',
    name='Test Template',
    from_email='test@test.com',
    subject='Test email template!',
    html='<b>This is a test email template!</b>'
)

print(response)
