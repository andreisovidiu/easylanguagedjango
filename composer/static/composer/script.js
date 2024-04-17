document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[type="submit"]').disabled = true;
    document.querySelector('input[type="number"]').addEventListener('keyup', function() {
        if(document.querySelector('input[type="number"]').value != 0) {
            document.querySelector('input[type="submit"]').disabled = false;
        } else {
            document.querySelector('input[type="submit"]').disabled = true;
        }
    });
});