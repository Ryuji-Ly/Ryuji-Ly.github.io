document.addEventListener("DOMContentLoaded", () => {
    const mazeContainer = document.getElementById("mazeContainer");
    const widthInput = document.getElementById("mazeWidth");
    const heightInput = document.getElementById("mazeHeight");
    const generateButton = document.getElementById("generateButton");
    const startButton = document.getElementById("startButton");
    const stopButton = document.getElementById("stopButton");

    let mazeWidth = parseInt(widthInput.value);
    let mazeHeight = parseInt(heightInput.value);
    let grid = [];
    let originNode = { x: mazeWidth - 1, y: mazeHeight - 1 };
    let interval;

    const directions = {
        right: { x: 1, y: 0, class: "no-right", opposite: "no-left" },
        left: { x: -1, y: 0, class: "no-left", opposite: "no-right" },
        down: { x: 0, y: 1, class: "no-bottom", opposite: "no-top" },
        up: { x: 0, y: -1, class: "no-top", opposite: "no-bottom" },
        nowhere: null,
    };

    function initializeGrid() {
        grid = [];
        mazeContainer.innerHTML = "";
        mazeContainer.style.gridTemplateColumns = `repeat(${mazeWidth}, 30px)`;
        mazeContainer.style.gridTemplateRows = `repeat(${mazeHeight}, 30px)`;

        for (let y = 0; y < mazeHeight; y++) {
            const row = [];
            for (let x = 0; x < mazeWidth; x++) {
                const cell = document.createElement("div");
                cell.classList.add("cell");
                mazeContainer.appendChild(cell);

                // Set initial direction
                let direction = directions.right;
                if (x === mazeWidth - 1 && y < mazeHeight - 1) {
                    direction = directions.down;
                } else if (x === mazeWidth - 1 && y === mazeHeight - 1) {
                    direction = directions.nowhere;
                    cell.classList.add("origin");
                }

                row.push({ x, y, element: cell, direction });
            }
            grid.push(row);
        }

        // Set the origin node at the bottom right corner
        originNode = { x: mazeWidth - 1, y: mazeHeight - 1 };
    }

    function step() {
        const currentOrigin = grid[originNode.y][originNode.x];

        // Get valid neighboring cells
        const neighbors = [];
        for (let dirKey in directions) {
            const d = directions[dirKey];
            if (d) {
                const newX = originNode.x + d.x;
                const newY = originNode.y + d.y;
                if (newX >= 0 && newX < mazeWidth && newY >= 0 && newY < mazeHeight) {
                    neighbors.push({ x: newX, y: newY, direction: d });
                }
            }
        }

        const nextNode = neighbors[Math.floor(Math.random() * neighbors.length)];

        // Update directions
        currentOrigin.direction = nextNode.direction;
        grid[nextNode.y][nextNode.x].direction = directions.nowhere;

        // Set new origin node
        grid[originNode.y][originNode.x].element.classList.remove("origin");
        originNode = { x: nextNode.x, y: nextNode.y };
        grid[originNode.y][originNode.x].element.classList.add("origin");

        // Redraw the walls
        readdWallsAroundOrigin();
        updateWallsAroundOrigin();
        updateCornersAroundOrigin();
    }

    function addCorners() {
        for (let y = 0; y < mazeHeight; y++) {
            for (let x = 0; x < mazeWidth; x++) {
                const cell = grid[y][x];
                const element = cell.element;
                const hasTop = element.classList.contains("no-top");
                const hasRight = element.classList.contains("no-right");
                const hasBottom = element.classList.contains("no-bottom");
                const hasLeft = element.classList.contains("no-left");
                addCorner(cell, "top-left");
                addCorner(cell, "top-right");
                addCorner(cell, "bottom-left");
                addCorner(cell, "bottom-right");
                if (hasTop && hasRight && hasBottom && hasLeft) {
                    continue;
                } else if (hasTop && hasLeft && hasBottom && !hasRight) {
                    removeCorner(element, "top-right");
                    removeCorner(element, "bottom-right");
                } else if (hasTop && hasRight && hasBottom && !hasLeft) {
                    removeCorner(element, "top-left");
                    removeCorner(element, "bottom-left");
                } else if (hasTop && hasRight && hasLeft && !hasBottom) {
                    removeCorner(element, "bottom-left");
                    removeCorner(element, "bottom-right");
                } else if (hasRight && hasBottom && hasLeft && !hasTop) {
                    removeCorner(element, "top-left");
                    removeCorner(element, "top-right");
                } else if (hasTop && hasRight && !hasLeft && !hasBottom) {
                    removeCorner(element, "top-left");
                    removeCorner(element, "bottom-left");
                    removeCorner(element, "bottom-right");
                } else if (hasTop && hasLeft && !hasRight && !hasBottom) {
                    removeCorner(element, "top-right");
                    removeCorner(element, "bottom-right");
                    removeCorner(element, "bottom-left");
                } else if (hasBottom && hasRight && !hasLeft && !hasTop) {
                    removeCorner(element, "top-left");
                    removeCorner(element, "top-right");
                    removeCorner(element, "bottom-left");
                } else if (hasBottom && hasLeft && !hasRight && !hasTop) {
                    removeCorner(element, "top-left");
                    removeCorner(element, "top-right");
                    removeCorner(element, "bottom-right");
                } else {
                    removeCorner(element, "top-left");
                    removeCorner(element, "top-right");
                    removeCorner(element, "bottom-left");
                    removeCorner(element, "bottom-right");
                }
            }
        }
    }

    function updateCornersAroundOrigin() {
        // Define the range around the origin node (5x5 grid around the origin)
        const startX = Math.max(0, originNode.x - 2);
        const endX = Math.min(mazeWidth - 1, originNode.x + 2);
        const startY = Math.max(0, originNode.y - 2);
        const endY = Math.min(mazeHeight - 1, originNode.y + 2);

        // Loop through the 5x5 grid around the origin
        for (let y = startY; y <= endY; y++) {
            for (let x = startX; x <= endX; x++) {
                const cell = grid[y][x];
                const element = cell.element;

                // Determine whether walls are present
                const hasTop = element.classList.contains("no-top");
                const hasRight = element.classList.contains("no-right");
                const hasBottom = element.classList.contains("no-bottom");
                const hasLeft = element.classList.contains("no-left");

                // Remove all corners initially to clean up any unwanted ones
                removeCorner(element, "top-left");
                removeCorner(element, "top-right");
                removeCorner(element, "bottom-left");
                removeCorner(element, "bottom-right");

                // Add corners based on current wall configuration
                if (hasTop && hasLeft) {
                    addCorner(cell, "top-left");
                }
                if (hasTop && hasRight) {
                    addCorner(cell, "top-right");
                }
                if (hasBottom && hasLeft) {
                    addCorner(cell, "bottom-left");
                }
                if (hasBottom && hasRight) {
                    addCorner(cell, "bottom-right");
                }
            }
        }
    }

    function addCorner(cell, position) {
        // Ensure the corner isn't already added
        if (!cell.element.querySelector(`.corner.${position}`)) {
            const corner = document.createElement("div");
            corner.classList.add("corner", position);
            cell.element.appendChild(corner);
        }
    }
    function removeCorner(element, position) {
        const corner = element.querySelector(`.corner.${position}`);
        if (corner) {
            element.removeChild(corner);
        }
    }

    function readdWallsAroundOrigin() {
        const startX = Math.max(0, originNode.x - 1);
        const endX = Math.min(mazeWidth - 1, originNode.x + 1);
        const startY = Math.max(0, originNode.y - 1);
        const endY = Math.min(mazeHeight - 1, originNode.y + 1);

        // Loop through the 3x3 grid around the origin
        for (let y = startY; y <= endY; y++) {
            for (let x = startX; x <= endX; x++) {
                const cell = grid[y][x];
                cell.element.classList.remove("no-top", "no-right", "no-bottom", "no-left");
            }
        }
    }

    function updateWallsAroundOrigin() {
        const startX = Math.max(0, originNode.x - 2);
        const endX = Math.min(mazeWidth - 1, originNode.x + 2);
        const startY = Math.max(0, originNode.y - 2);
        const endY = Math.min(mazeHeight - 1, originNode.y + 2);
        for (let y = startY; y <= endY; y++) {
            for (let x = startX; x <= endX; x++) {
                const cell = grid[y][x];
                const { direction } = cell;
                if (direction && direction !== directions.nowhere) {
                    cell.element.classList.add(direction.class);
                    const neighborX = x + direction.x;
                    const neighborY = y + direction.y;
                    if (
                        neighborX >= 0 &&
                        neighborX < mazeWidth &&
                        neighborY >= 0 &&
                        neighborY < mazeHeight
                    ) {
                        grid[neighborY][neighborX].element.classList.add(direction.opposite);
                    }
                }
            }
        }
    }

    function redrawWalls() {
        for (let y = 0; y < mazeHeight; y++) {
            for (let x = 0; x < mazeWidth; x++) {
                const cell = grid[y][x];
                cell.element.classList.remove("no-top", "no-right", "no-bottom", "no-left");
            }
        }
        for (let y = 0; y < mazeHeight; y++) {
            for (let x = 0; x < mazeWidth; x++) {
                const cell = grid[y][x];
                const { direction } = cell;
                if (direction && direction !== directions.nowhere) {
                    cell.element.classList.add(direction.class);
                    const neighborX = x + direction.x;
                    const neighborY = y + direction.y;
                    if (
                        neighborX >= 0 &&
                        neighborX < mazeWidth &&
                        neighborY >= 0 &&
                        neighborY < mazeHeight
                    ) {
                        grid[neighborY][neighborX].element.classList.add(direction.opposite);
                    }
                }
            }
        }
    }

    generateButton.addEventListener("click", () => {
        mazeWidth = parseInt(widthInput.value);
        mazeHeight = parseInt(heightInput.value);
        initializeGrid();
        redrawWalls(); // Draw the initial walls
        addCorners();
    });

    startButton.addEventListener("click", () => {
        if (interval) return;
        interval = setInterval(step, 10); // Adjust interval speed as needed
        startButton.disabled = true;
        stopButton.disabled = false;
    });

    stopButton.addEventListener("click", () => {
        clearInterval(interval);
        interval = null;
        startButton.disabled = false;
        stopButton.disabled = true;
    });

    // Initialize the grid on load
    initializeGrid();
    redrawWalls(); // Draw the initial walls
    addCorners();
});
