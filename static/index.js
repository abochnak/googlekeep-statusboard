function checkFunction(ths, index) { 
    var checked = ths.checked;
    var token = document.body.getAttribute('data-token');
    var list = document.body.getAttribute('data-list');
    var v = document.getElementById("text-" + index); 
    var checkeditems = document.getElementById("checked-items");
    var uncheckeditems = document.getElementById("unchecked-items");

    fetch('/' + token + '/check', {
        method: "post",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "index": parseInt(index)-1,
            "name": v.innerHTML,
            "checked": (checked?"true":"false"),
            "list": list
        })
    })
    .then(d => d.text())
    .then(function(d) {
        console.log("check:" + d);
        var p = ths.parentElement.parentElement;
        if(checked){
            checkeditems.appendChild(p);
            v.classList.add("crossed");
            if (checkeditems.querySelectorAll("p").length == 1) {
                checkeditems.innerHTML = '<hr>' + checkeditems.innerHTML;
            }
        }
        else{
            uncheckeditems.appendChild(p);
            v.classList.remove("crossed"); 

            if (checkeditems.querySelectorAll("p").length == 0) {
                checkeditems.querySelector("hr").remove();
            }
        }
    })
 
} 
