// var foldBtns = document.getElementsByClassName("fold-button");
//
// for (var i = 0; i < foldBtns.length; i++) {
//     foldBtns[i].addEventListener("click", function(event) {
//         console.log("you clicked ", event.target);
//
//         var post = event.target.parentElement.parentElement;
//         var info = post.getElementsByClassName("article-info")[0];
//         var text = post.getElementsByClassName("article-text")[0];
//
//         if (info.style.display === "none") {
//             info.style.display = "block";
//             text.style.display = "block";
//             event.target.textContent = "Свернуть";
//         } else {
//             info.style.display = "none";
//             text.style.display = "none";
//             event.target.textContent = "Развернуть";
//         }
//     });
// }

var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        var post = event.target.closest('.one-post');
        post.classList.toggle('folded');

        event.target.textContent = post.classList.contains('folded') ? "Развернуть" : "Свернуть";
    });
}