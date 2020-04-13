    OSName="Unknown OS"
    if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";
    if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS";
    if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX";
    if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";
    console.log(OSName);
    window.onhashchange = function() {
     // location.reload();
    }

    $(document).on('keyup keydown', function(e){
        if (navigator.appVersion.indexOf("Mac")!=-1){
            
        if(e.shiftKey){
            var url = "/mapping/not-found";
            $(location).attr('href',url);
        }
        }
    });

    function copyToClipboard() {
     // Create a "hidden" input
     var aux = document.createElement("input");
     // Assign it the value of the specified element
     aux.setAttribute("value", "Preentscreen!");
     // Append it to the body
     document.body.appendChild(aux);
     // Highlight its content
     aux.select();
     // Copy the highlighted text
     document.execCommand("copy");
     // Remove it from the body
     document.body.removeChild(aux);
     alert("Print screen disabled.");
    }

    $(window).keyup(function(e){
     if(e.keyCode == 44){
       copyToClipboard();
     }
    });

    // $(window).focus(function() {
    //  $("body").show();
    // }).blur(function() {
    //    // $(location).attr('href','https://mapsee.io/dashboard');
    //    $(location).attr('href','https://mapsee.io/dashboard');
    //  // $("body").hide();
    // });