function sendMail(contactForm) {
    console.log("emailjs.send");
    emailjs.send("service_vg0sszf", "template_4p3bsdl", 
    {
        "from_name": contactForm.contact_name.value,
        "from_email": contactForm.contact_epost.value,
        "message": contactForm.contact_message.value
    });

    /*.then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
     }, function(error) {
        console.log('FAILED...', error);
     });*/
     return false;
}