# PassVar

PassVar is a simple python library used for varifying and generating passwords
based on OWASP and IBM standard.
PassVar has two basic engimes.
1. Generator
2. Varification

### Passowrd Generation
Generator engine is used to generate a pseudo random password
according to most commonly used standards.
According to OWASP and IBM standards a strong type
password is composed of **ASCII alphabet characters**,
**ASCII numeric** and **ASCII special characters** with some exception.

### Password Verification
Password varification is a process for varifying whether a password is
- **Weak**
- **Normal**
- **String**
- **Very Strong**

#### Passwords are classified based on the following criterias.
1. **Length**
2. **Content**

1. **Length**
According to **OWASP** password length can be classified as weak or strong.
The standard specifies that the minimum password length should be **8**.
Password with length lessthan 8 is generally considered to be a weak password.

2. **Content**
This property of a password allows to have a password with a variety
of characters rather than similar and repetitive characters in the password.
