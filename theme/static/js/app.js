document.addEventListener('DOMContentLoaded', function() {
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    document.getElementById('startDictation').addEventListener('click', function() {
        recognition.start();
    });

    recognition.onresult = function(event) {
        var transcript = event.results[0][0].transcript;
        var amountField = document.getElementById('amount');
        var descriptionField = document.getElementById('description');
        // Debug statements to check if form fields are found
        console.log("Amount Field:", amountField);
        console.log("Description Field:", descriptionField);


        // Split transcript into amount and description
        var parts = transcript.split(' ');
        var amount = parseFloat(parts[2]);
        var description = parts.slice(3).join(' ');

        // Fill the form fields with speech recognition results
        if (amountField && descriptionField) {
            amountField.value = amount.toFixed(2);
            descriptionField.value = description;

            // Submit the form
            document.getElementById('forms').submit();
        } else {
            console.log("Form fields not found");
        }
        
    };

    recognition.onerror = function(event) {
        console.log('Error occurred in recognition: ' + event.error);
    };
});