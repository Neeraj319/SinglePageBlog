const containerDIv = document.querySelector(".container");
const mainDiv = document.createElement("div");
const addBlog = document.querySelector(".add-blog");

containerDIv.appendChild(mainDiv);
mainDiv.classList.add("main-div");

document.addEventListener("DOMContentLoaded", allBlogs);

addBlog.addEventListener("click", addForm);

function allBlogs() {
  fetch("http://127.0.0.1:8000/", {
    method: "GET",
    headers: {
      Authorization: "Token c4b57ca0c6a0fe6e60806cf4357735999a9e0047",
    },
  })
    .then((res) => {
      console.log(res.body);
      if (res.ok) {
        res.json().then((data) => {
          for (blog of data) {
            const blogDiv = document.createElement("div");
            const addPara = document.createElement("p");
            const like = document.createElement("span");
            const likeButton = document.createElement("button");
            likeButton.innerHTML = '<i class="fas fa-thumbs-up fa-small"></i>';
            likeButton.classList.add("like-button");
            like.classList.add("like");
            blogDiv.classList.add("blog-div");
            blogDiv.innerText = `${blog.title}`;
            addPara.innerText = `${blog.body}`;
            like.innerText = `likes: ${blog.likes.length}`;
            mainDiv.appendChild(blogDiv);
            blogDiv.appendChild(addPara);
            blogDiv.appendChild(like);
            blogDiv.appendChild(likeButton);
          }
        });
      } else {
        console.log(res);
      }
    })
    .catch((error) => {
      console.log("some error occurred");
    });
}

let isForm = false;

function addForm(e) {
  // mainDiv.remove();
  isForm = !isForm;
  e.target.innerText = isForm ? "home" : "add blog";
  if (isForm) {
    const formDiv = document.querySelector(".form-div");
    mainDiv.style.display = "none";
    if (formDiv) {
      formDiv.style.display = "block";
      return;
    }
    const formDIv = document.createElement("div");
    formDIv.classList.add("form-div");
    containerDIv.appendChild(formDIv);
    const titleInput = document.createElement("input");
    const addTitleLabel = document.createElement("label");
    titleInput.classList.add("form-control", "input");
    addTitleLabel.innerHTML = "Title of blog";
    addTitleLabel.classList.add("text-white");
    formDIv.appendChild(addTitleLabel);
    formDIv.appendChild(titleInput);
    const addBodyLabel = document.createElement("label");
    addBodyLabel.innerHTML = "Content";
    addBodyLabel.classList.add("text-white");
    formDIv.appendChild(addBodyLabel);
    const bodyTextArea = document.createElement("textarea");
    bodyTextArea.classList.add("form-control", "body");
    bodyTextArea.setAttribute("rows", "7");
    formDIv.appendChild(bodyTextArea);
    mainDiv.appendChild(document.createElement("br"));
    const addBlogButton = document.createElement("button");

    addBlogButton.classList.add("btn", "btn-primary", "btn-lg", "btn-block");
    addBlogButton.innerHTML = "add blog";
    formDIv.appendChild(addBlogButton);
    const addBlogButtonP = document.querySelector(".btn-primary");
    addBlogButtonP.addEventListener("click", postBlog);
  } else {
    const formDiv = document.querySelector(".form-div");
    formDiv.style.display = "none";
    mainDiv.style.display = "block";
  }
}

function postBlog() {
  const title = document.querySelector(".input");
  const body = document.querySelector(".body");
  if (title.value && body.value) {
    fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token c4b57ca0c6a0fe6e60806cf4357735999a9e0047",
      },
      body: JSON.stringify({
        title: title.value,
        body: body.value,
      }),
    })
      .then((res) => {
        if (res.ok) {
          res.json().then((data) => {
            const formDIv = document.querySelector(".form-div");
            formDIv.remove();
            allBlogs();
          });
        } else {
          console.log("error occured");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
