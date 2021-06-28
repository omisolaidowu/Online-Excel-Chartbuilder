// (design, name, map_fun, reduce_fun=None, language='javascript', wrapper=None, **defaults)
// active_users_view = ViewDefinition('content'
//     function (doc) {
        
//             emit(doc.content, doc)
//     })


// Image file downloader:

var but = document.getElementById("btn");

but.onclick=()=>{
        var text = document.getElementById("image").src; 
        console.log(text)
        var filename = "output.png";
        download(filename, text);
                  }
      

function download(filename, textInput) {

                  var element = document.createElement('a');
                  element.setAttribute('href', textInput);
                  element.setAttribute('download', filename);
                  document.body.appendChild(element);
                 element.click();
                  //document.body.removeChild(element);
            }

