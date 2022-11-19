
    function copyText() {

        /* Select text area by id*/
        var span = document.getElementById("psw");

        /* Copy selected text into clipboard */
        navigator.clipboard.writeText(span.innerText);

        /* Generate alert when psw copied to clipboard */
        alert("Password copied to clipboard");
    }
