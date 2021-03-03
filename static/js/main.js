let dropdown = document.querySelectorAll(".menu__item");
for (let i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("mouseenter", showSub, false);
  dropdown[i].addEventListener("mouseleave", hideSub, false);
}

function showSub() {
  if (this.children.length > 1) {
    this.children[1].style.height = "auto";
    this.children[1].style.opacity = "1";
    this.children[1].style.overflow = "visible";
  } else {
    return false;
  }
}

function hideSub() {
  if (this.children.length > 1) {
    this.children[1].style.height = "0";
    this.children[1].style.opacity = "0";
    this.children[1].style.overflow = "hidden";
  } else {
    return false;
  }
}
