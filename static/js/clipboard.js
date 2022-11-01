
    function copyText() {

        /* Select text area by id*/
        var span = document.getElementById("psw");

        /* Copy selected text into clipboard */
        navigator.clipboard.writeText(span.innerText);

        /* Set the copied text as text for
        div with id clipboard */
        document.getElementById("feedback")
              .innerHTML = "Password copied to clipboard!";
    }
