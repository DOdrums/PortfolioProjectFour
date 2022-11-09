document.getElementById('navbar-toggler').addEventListener("click", collapsed)
function collapsed() {
    closed = $('#navbar-toggler').hasClass('collapsed')
    if(closed === false) {
    console.log("collapsed!")
    } else {
        console.log("JA!")
    }
}