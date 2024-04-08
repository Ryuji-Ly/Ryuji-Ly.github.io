class GameOfLife {
    constructor(gridSize, seed, cellSize) {
        this.gridSize = gridSize;
        this.seed = seed;
        this.cellSize = cellSize;
        this.initializeGrid();
    }
    initializeGrid() {
        this.grid = new Array(this.gridSize).fill(null).map(() => new Array(this.gridSize).fill(0));

        this.setSeed(this.seed);
    }
    setSeed(seed) {
        const rng = new Math.seedrandom(seed);

        for (let y = 0; y < this.gridSize; y++) {
            for (let x = 0; x < this.gridSize; x++) {
                if (rng.quick() < 0.3) {
                    this.grid[y][x] = 1;
                }
            }
        }
    }
    update() {
        const newGrid = new Array(this.gridSize)
            .fill(null)
            .map(() => new Array(this.gridSize).fill(0));
        for (let y = 0; y < this.gridSize; y++) {
            for (let x = 0; x < this.gridSize; x++) {
                const neighbors = this.countAliveNeighbors(x, y);

                if (this.grid[y][x] === 1) {
                    if (neighbors < 2 || neighbors > 3) {
                        newGrid[y][x] = 0;
                    } else {
                        newGrid[y][x] = 1;
                    }
                } else {
                    if (neighbors === 3) {
                        newGrid[y][x] = 1;
                    }
                }
            }
        }
        this.grid = newGrid;
    }
    countAliveNeighbors(x, y) {
        let count = 0;
        const directions = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ];
        for (const [dx, dy] of directions) {
            const nx = (x + dx + this.gridSize) % this.gridSize;
            const ny = (y + dy + this.gridSize) % this.gridSize;
            if (this.grid[ny][nx] === 1) {
                count++;
            }
        }
        return count;
    }
    draw(ctx) {
        const cellSize = this.cellSize;
        const gridSize = this.gridSize;
        ctx.clearRect(0, 0, gridSize * cellSize, gridSize * cellSize);
        ctx.strokeStyle = "#000000";
        ctx.lineWidth = 1;
        for (let y = 0; y <= gridSize; y++) {
            const yPos = y * cellSize + 0.5;
            ctx.beginPath();
            ctx.moveTo(0, yPos);
            ctx.lineTo(gridSize * cellSize, yPos);
            ctx.stroke();
        }
        for (let x = 0; x <= gridSize; x++) {
            const xPos = x * cellSize + 0.5;
            ctx.beginPath();
            ctx.moveTo(xPos, 0);
            ctx.lineTo(xPos, gridSize * cellSize);
            ctx.stroke();
        }
        for (let y = 0; y < gridSize; y++) {
            for (let x = 0; x < gridSize; x++) {
                if (this.grid[y][x] === 1) {
                    const xPos = x * cellSize;
                    const yPos = y * cellSize;
                    ctx.fillStyle = "#FFFFFF";
                    ctx.fillRect(xPos, yPos, cellSize, cellSize);
                }
            }
        }
    }
}

function startGame() {
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");
    const marginPercentage = 0.05;
    const gridSize = parseInt(document.getElementById("gridSize").value);
    const seed = document.getElementById("seed").value;
    const availableWidth = window.innerWidth * (1 - marginPercentage * 2);
    const availableHeight = window.innerHeight * (1 - marginPercentage * 2);
    const maxSize = Math.min(availableWidth, availableHeight);
    canvas.width = maxSize;
    canvas.height = maxSize;
    const cellSize = maxSize / gridSize;
    const game = new GameOfLife(gridSize, seed, cellSize);

    function gameLoop() {
        game.update();
        game.draw(ctx);
        requestAnimationFrame(gameLoop);
    }

    gameLoop();
}
