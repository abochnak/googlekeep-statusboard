function checkFunction(checked, index) { 
    var token = document.body.getAttribute('data-token');
    var v = document.getElementById("text-" + index); 
    

    fetch('/' + token + '/check', {
        method: "post",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "index": parseInt(index)-1,
            "name": v.innerHTML,
            "checked": (checked?"true":"false")
        })
    }).then(function(d) {
        console.log(d);
        if(checked){
            v.classList.add("crossed");
        }
        else{
            v.classList.remove("crossed"); 
        }
    })
 
} 