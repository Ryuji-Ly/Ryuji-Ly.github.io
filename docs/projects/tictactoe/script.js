document.addEventListener("DOMContentLoaded", () => {
    const cells = document.querySelectorAll(".cell");
    const onePlayerButton = document.getElementById("one-player");
    const twoPlayerButton = document.getElementById("two-player");
    const twoPlayerSpecialButton = document.getElementById("two-player-special");
    const gameModeDisplay = document.getElementById("game-mode");
    const twoPlayerTurnDisplay = document.getElementById("two-player-turn");
    twoPlayerSpecialButton.style.display = "none";
    twoPlayerTurnDisplay.style.display = "none";
    let currentPlayer = "X";
    let gameState = ["", "", "", "", "", "", "", "", ""];
    let isGameActive = true;
    let gameMode = "1 Player";

    const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    onePlayerButton.addEventListener("click", () => setGameMode("1 Player"));
    twoPlayerButton.addEventListener("click", () => setGameMode("2 Player"));

    function setGameMode(mode) {
        gameMode = mode;
        gameModeDisplay.textContent = `Current Game Mode: ${gameMode}`;
        if (gameMode === "1 Player") {
            twoPlayerTurnDisplay.style.display = "none";
        } else {
            twoPlayerTurnDisplay.style.display = gameMode === "2 Player" ? "block" : "none";
            updateTurnDisplay();
        }
        resetGame();
    }

    cells.forEach((cell) => {
        cell.addEventListener("click", handleCellClick);
    });

    function handleCellClick(event) {
        const cell = event.target;
        const cellIndex = parseInt(cell.getAttribute("data-index"));

        if (gameState[cellIndex] !== "" || !isGameActive) {
            return;
        }

        gameState[cellIndex] = currentPlayer;
        cell.textContent = currentPlayer;
        checkWinner();

        if (gameMode === "1 Player" && isGameActive) {
            currentPlayer = "O";
            setTimeout(cpuMove, 500);
        } else {
            currentPlayer = currentPlayer === "X" ? "O" : "X";
            updateTurnDisplay();
        }
    }

    function cpuMove() {
        let bestMove = getBestMove();
        gameState[bestMove] = currentPlayer;
        cells[bestMove].textContent = currentPlayer;
        checkWinner();
        currentPlayer = "X";
    }

    function getBestMove() {
        for (let i = 0; i < winningCombinations.length; i++) {
            const [a, b, c] = winningCombinations[i];
            if (gameState[a] === "O" && gameState[b] === "O" && gameState[c] === "") return c;
            if (gameState[a] === "O" && gameState[b] === "" && gameState[c] === "O") return b;
            if (gameState[a] === "" && gameState[b] === "O" && gameState[c] === "O") return a;
        }
        for (let i = 0; i < winningCombinations.length; i++) {
            const [a, b, c] = winningCombinations[i];
            if (gameState[a] === "X" && gameState[b] === "X" && gameState[c] === "") return c;
            if (gameState[a] === "X" && gameState[b] === "" && gameState[c] === "X") return b;
            if (gameState[a] === "" && gameState[b] === "X" && gameState[c] === "X") return a;
        }
        let availableCells = gameState
            .map((value, index) => (value === "" ? index : null))
            .filter((value) => value !== null);
        return availableCells[Math.floor(Math.random() * availableCells.length)];
    }

    function checkWinner() {
        let roundWon = false;

        for (let i = 0; i < winningCombinations.length; i++) {
            const [a, b, c] = winningCombinations[i];
            if (gameState[a] && gameState[a] === gameState[b] && gameState[a] === gameState[c]) {
                roundWon = true;
                break;
            }
        }

        if (roundWon) {
            alert(`Player ${currentPlayer} has won!`);
            resetGame();
            return;
        }

        if (!gameState.includes("")) {
            alert("Draw!");
            resetGame();
            return;
        }
    }

    function resetGame() {
        gameState = ["", "", "", "", "", "", "", "", ""];
        cells.forEach((cell) => (cell.textContent = ""));
        currentPlayer = "X";
        isGameActive = true;
    }

    function updateTurnDisplay() {
        if (gameMode === "2 Player") {
            twoPlayerTurnDisplay.textContent = `Current Turn: Player ${currentPlayer}`;
        }
    }

    document.getElementById("game-board").addEventListener("dblclick", resetGame);
});
