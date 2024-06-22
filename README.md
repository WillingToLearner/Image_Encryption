# IMAGE ENCRYPTION AND DECRYPTION USING CONFUSION AND DIFFUSION TECHNIQUES

1.	ABSTRACT:
   
Image encryption converts an original image into an encrypted form, preventing unauthorized
access, ensuring its confidentiality during transmission or storage. Blurring and diffusion
techniques, utilizing complex mathematical algorithms, are employed to mix and hash image
data, imparting high entropy and making changes in the ciphertext significantly impact the
encrypted image. During encryption, obfuscation complicates input-output relations, employing
substitution or permutation to generate seemingly random output. In diffusion, methods like
pixel movement, rotation, or XOR with a key spread and mix data to affect the entire image with
a single pixel change. Decryption reverses encryption steps, requiring a decryption key for
authorized access. This process maintains a high level of security, resisting brute force or
statistical attacks, as a single pixel alteration impacts the entire image. Hence, utilizing
obfuscation and diffusion techniques is an effective method for securing image confidentiality
during transmission or storage.

2. INTRODUCTION:

In the dynamic sphere of data security, the perpetual balancing act between safeguarding
sensitive information and its susceptibility to threats endures. The contemporary era, heavily
reliant on the internet, witnesses an exponential surge in data volume, intensifying the urgency to
ensure secure data transmission and storage. As data travels across the internet, the looming
specter of potential attacks poses a considerable risk to the confidentiality and integrity of
information. Hence, modern cryptographic algorithms play a pivotal role in fortifying data
security, ensuring both confidentiality and integrity.
Two primary encryption methods come into play: Public-key cryptography and Private-key
cryptography. Public-key cryptography employs a shared and a secret key, enabling secure data
transfer and verification. Conversely, private-key cryptography relies on a singular secret key for
encryption and decryption, safeguarding sensitive data.
A significant portion of internet-transmitted data comprises images, often containing sensitive
personal information that could compromise privacy. Consequently, there's a growing urgency to
ensure image security during both transmission and storage.

Chaotic maps, mathematical formulas producing sequences of highly unpredictable numbers,
enhance image encryption by generating vastly different outcomes with minimal alterations in
initial conditions, fortifying the security and privacy of the process.
The proposed encryption method for RGB images in this paper employs public-key
cryptography, eliminating the need for a pre-shared private key between parties. By manipulating
pixel values through a blend of Confusion and Diffusion—incorporating Arnold’s Cat map and
Henon’s map—the aim is to fortify the image's integrity and confidentiality, making it resilient
against diverse attacks.
