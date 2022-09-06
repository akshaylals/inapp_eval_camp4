// navdrawer options
const navOptions = {
    'edge': 'left'
}

// navdrawer click
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, navOptions);
});

// Select
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
});


// Pagination rows select
function pageRows(url) {
    const rows = event.target.value
    window.location.href =  url + `?rows=${rows}`
}


// Tooltips
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, {});
});