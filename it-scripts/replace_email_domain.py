def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

new_email = replace_domain("david.benitez@usach.cl", "usach.cl", "googlecloud.com")
print(new_email)