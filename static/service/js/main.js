const tabs = document.querySelectorAll(".tab-head");
const tabContents = document.querySelectorAll(".tab-content");

tabs[0].classList.add("active");
tabContents[0].classList.add("active");
// add click event listener to each tab
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    console.log("111");
    // remove active class from all tabs and tab contents
    tabs.forEach((tab) => tab.classList.remove("active"));
    tabContents.forEach((content) => content.classList.remove("active"));

    // add active class to clicked tab and corresponding tab content
    tab.classList.add("active");
    const tabId = tab.dataset.tab;
    const tabContent = document.querySelector(
      `.tab-content[data-tab="${tabId}"]`
    );
    tabContent.classList.add("active");
  });
});
