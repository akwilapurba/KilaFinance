document.addEventListener('DOMContentLoaded', function() {
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    document.getElementById('startDictation').addEventListener('click', function() {
        recognition.start();
    });

    document.getElementById('resetFields').addEventListener('click', function() {
        // Reset amount field
        var amountField = document.getElementById('amount');
        if (amountField) {
            amountField.value = '';
        }
        // Reset description field
        var descriptionField = document.getElementById('description');
        if (descriptionField) {
            descriptionField.value = '';
        }
    });

    recognition.onresult = function(event) {
        var transcript = event.results[0][0].transcript;

        // Remove commas from the transcript
        transcript = transcript.replace(/,/g, '');

        // Regular expression to match numbers in the transcript
        var amountMatch = transcript.match(/\d+(\.\d+)?/);
        var amount = parseFloat(amountMatch[0]);

        // Fill the amount field with speech recognition result
        var amountField = document.getElementById('amount');
        if (amountField) {
            amountField.value = amount.toFixed(2);
        } else {
            console.log("Amount Field not found");
        }

        // Extracting description from transcript
        var description = transcript.replace(amountMatch[0], '').trim();
        var descriptionField = document.getElementById('description');
        if (descriptionField) {
            descriptionField.value = description;
        } else {
            console.log("Description Field not found");
        }

        // Submit the form
        document.getElementById('forms').submit();
    };

    recognition.onerror = function(event) {
        console.log('Error occurred in recognition: ' + event.error);
    };
});