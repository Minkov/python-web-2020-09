function expandCollapse() {
    let collapseContainer = this.parentElement;
    while (this) {
        if (collapseContainer.className.indexOf('collapse-container') >= 0) {
            break;
        }

        collapseContainer = collapseContainer.parentElement;
    }

    if (collapseContainer.className.indexOf('collapsed') < 0) {
        this.parentElement.className += ' collapsed';
    } else {
        collapseContainer.className =
            this.parentElement.className.replace('collapsed', '');
    }
}

function initExpand() {
    const items = [...document.getElementsByClassName('collapse-toggle')];
    items.forEach(item => {
        item.addEventListener('click', expandCollapse);
    });
}

initExpand();