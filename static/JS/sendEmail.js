function sendMail(contactForm) {
    
    var templateParams = {
        from_name: contactForm.contact_name.value,
        from_email: contactForm.contact_mail.value,
        project_request: contactForm.contact_message.value
    };
    
    emailjs.send("service_vg0sszf", 
        "template_4p3bsdl", 
        templateParams
        ).then(function(response) {
            console.log('SUCCESS!', response.status, response.text);
        }, function(error) {
            console.log('FAILED...', error);
     });
     return false;
}