const containerDIv = document.querySelector(".container");
const mainDiv = document.createElement("div");
const addBlog = document.querySelector(".add-blog");

var token = document.cookie.split("=");
token = token[0] + " " + token[1];
containerDIv.appendChild(mainDiv);
mainDiv.classList.add("main-div");

document.addEventListener("DOMContentLoaded", allBlogs);

addBlog.addEventListener("click", addForm);

function allBlogs() {
  fetch("http://127.0.0.1:8000/", {
    method: "GET",
    headers: {
      Authorization: token,
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
        if (res.status == 401) {
          const loginDIv = document.createElement("div");
          loginDIv.classList.add("login-div");
          containerDIv.append(loginDIv);
          const usernameInput = document.createElement("input");
          usernameInput.setAttribute("placeholder", "username");
          usernameInput.classList.add("form-control", "username-input");
          loginDIv.appendChild(usernameInput);
          const passwordInput = document.createElement("input");
          passwordInput.setAttribute("type", "password");
          passwordInput.classList.add("form-control", "pass-input");
          passwordInput.setAttribute("placeholder", "password");
          loginDIv.appendChild(passwordInput);
          const loginButton = document.createElement("button");
          loginButton.classList.add("btn", "btn-white", "btn-lg", "btn-block");
          loginButton.innerText = "login";
          loginDIv.appendChild(loginButton);
          loginButton.addEventListener("click", login);
        }
      }
    })
    .catch((error) => {
      console.log("some error occurred");
    });
}

let isForm = false;

function addForm(e) {
  isForm = !isForm;
  e.target.innerText = isForm ? "home" : "add blog";
  if (isForm) {
    const formDiv = document.querySelector(".form-div");
    mainDiv.style.display = "none";
    // mainDiv.remove();
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
        Authorization: token,
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
            console.log("hello");
            allBlogs();
          });
        } else {
          console.log("error occured");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    alert("fields can't be empty");
  }
}

function login() {
  const usernameInput = document.querySelector(".username-input");
  const passwordInput = document.querySelector(".pass-input");
  if (usernameInput.value && passwordInput.value) {
    fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: usernameInput.value,
        password: passwordInput.value,
      }),
    }).then((res) => {
      if (res.ok) {
        res.json().then((token) => {
          saveToken(token);
          allBlogs();
        });
      } else {
        alert("invalid username or password");
      }
    });
  } else {
    alert("please provide the following credentials");
  }
}

function saveToken(token) {
  var now = new Date();
  var time = now.getTime();
  var expireTime = time + 1000 * 36000;
  now.setTime(expireTime);
  document.cookie = `Token =${token};expires=` + now.toUTCString() + ";path=/";
  //console.log(document.cookie);  // 'Wed, 31 Oct 2012 08:50:17 UTC'
}
// function signup(e) {
//   e.target.innerText = "login";
//   addBlog.addEventListener("click", login);
//   console.log("sign up page");
// }
