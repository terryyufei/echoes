// Toggling the menu bar 

const navItems = document.querySelector('.nav__items');
const openNavBtn = document.querySelector('#open__nav-btn');
const closeNavBtn = document.querySelector('#close__nav-btn');

// open dropdown menu 
const openNav = () => {
    navItems.style.display = 'flex';
    openNavBtn.style.display = 'none';
    closeNavBtn.style.display = 'inline-block'
}

// close dropdown menu 
const closeNav = () => {
    navItems.style.display = 'none';
    openNavBtn.style.display = 'inline-block';
    closeNavBtn.style.display = 'none'
}

openNavBtn.addEventListener('click', openNav);
closeNavBtn.addEventListener('click', closeNav);

// Side bar toggle
const sidebar = document.querySelector('aside');
const showSidebarBtn = document.querySelector('#show__sidebar-btn');
const hideSidebarBtn = document.querySelector('#hide__sidebar-btn');

// show sidebar on small devices
const showSidebar = () => {
    sidebar.style.left = '0';
    showSidebarBtn.style.display = 'none';
    hideSidebarBtn.style.display = 'inline-block';
}

// hide sidebar on small devices
const hideSidebar = () => {
    sidebar.style.left = '-100%';
    showSidebarBtn.style.display = 'inline-block';
    hideSidebarBtn.style.display = 'none';
}

showSidebarBtn.addEventListener('click', showSidebar);
hideSidebarBtn.addEventListener('click', hideSidebar);



// CKEDITOR.editorConfig = function( config ) {
        // config.uiColor = '#751313';
    // };


document.addEventListener('DOMContentLoaded', function () {
    CKEDITOR.replace('editor1');
    var editor = CKEDITOR.instances.editor1;
    if (editor) {
        editor.on('instanceReady', function (ev) {
            var editor = ev.editor;
            var body = editor.document.getBody();
            body.setStyle('background-color', 'blue');
            // Add more custom styles as needed
        });
    }
});
