const GameStates = {
    START_MENU: 0,
    PLAYING: 1,
    PAUSED: 2,
    GAME_OVER: 3,
};
const bossSpawn = 100;
let gameState = GameStates.START_MENU;
let score = 0;
let wave = 0;
let elapsedTime = 0;
let enemies = [];
let bullets = [];
let explosions = [];
let mines = [];
let healthPacks = [];
let currentBackgroundFrame = 0;
const bossImages = [
    "./assets/images/sprites/boss1.png",
    "./assets/images/sprites/boss2.png",
    "./assets/images/sprites/boss3.png",
];
const enemyImages = [
    "./assets/images/sprites/enemy1.png",
    "./assets/images/sprites/enemy2.png",
    "./assets/images/sprites/enemy3.png",
    "./assets/images/sprites/enemy4.png",
];
const bulletImages = [
    "./assets/images/sprites/bullets/bean.png",
    "./assets/images/sprites/bullets/plasma.png",
];
const explosionImages = [
    "./assets/images/sprites/explosion/1.png",
    "./assets/images/sprites/explosion/2.png",
    "./assets/images/sprites/explosion/3.png",
    "./assets/images/sprites/explosion/4.png",
    "./assets/images/sprites/explosion/5.png",
    "./assets/images/sprites/explosion/6.png",
    "./assets/images/sprites/explosion/7.png",
    "./assets/images/sprites/explosion/8.png",
    "./assets/images/sprites/explosion/9.png",
];
const laserImages = [
    "./assets/images/sprites/laser/frame_0.gif",
    "./assets/images/sprites/laser/frame_1.gif",
    "./assets/images/sprites/laser/frame_2.gif",
    "./assets/images/sprites/laser/frame_3.gif",
];
const backgroundFramesPath = [
    "./assets/images/backgrounds/frames/frame_00.gif",
    "./assets/images/backgrounds/frames/frame_01.gif",
    "./assets/images/backgrounds/frames/frame_02.gif",
    "./assets/images/backgrounds/frames/frame_03.gif",
    "./assets/images/backgrounds/frames/frame_04.gif",
    "./assets/images/backgrounds/frames/frame_05.gif",
    "./assets/images/backgrounds/frames/frame_06.gif",
    "./assets/images/backgrounds/frames/frame_07.gif",
    "./assets/images/backgrounds/frames/frame_08.gif",
    "./assets/images/backgrounds/frames/frame_09.gif",
    "./assets/images/backgrounds/frames/frame_10.gif",
    "./assets/images/backgrounds/frames/frame_11.gif",
    "./assets/images/backgrounds/frames/frame_12.gif",
    "./assets/images/backgrounds/frames/frame_13.gif",
    "./assets/images/backgrounds/frames/frame_14.gif",
    "./assets/images/backgrounds/frames/frame_15.gif",
];

class Player {
    constructor(x, y, width, height, speed, bulletSpeed, bulletFrequency) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.bulletSpeed = bulletSpeed;
        this.bulletFrequency = bulletFrequency;
        this.bullets = [];
        this.image = new Image();
        this.image.src = "./assets/images/sprites/spaceship.png";
    }

    update() {
        if (keys["ArrowLeft"] && this.x > 0) {
            this.x -= this.speed;
        }
        if (keys["ArrowRight"] && this.x < canvas.width - this.width) {
            this.x += this.speed;
        }
        if (keys["ArrowUp"] && this.y > 0) {
            this.y -= this.speed;
        }
        if (keys["ArrowDown"] && this.y < canvas.height - this.height) {
            this.y += this.speed;
        }

        this.shoot();
    }

    render(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
    }

    shoot() {
        if (frameCount % this.bulletFrequency === 0) {
            const bulletX = this.x + this.width / 2 - 15 / 2; // Center bullet horizontally under player
            const bulletY = this.y;
            const bullet = new Bullet(bulletX, bulletY, 15, 19, this.bulletSpeed); // Create bullet
            this.bullets.push(bullet);
        }
    }
}

class Bullet {
    constructor(x, y, width, height, speed) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.image = new Image();
        this.image.src = "./assets/images/sprites/bullets/bean.png";
    }

    update() {
        this.y -= this.speed;
    }

    render(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
    }
}

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const player = new Player(canvas.width / 2 - 25, canvas.height - 60, 40, 60, 5, 8, 6);
let keys = {};
let frameCount = 0;
let currentFrameIndex = 0;
const frameWidth = canvas.width;
const frameHeight = canvas.height;
const backgroundFrames = [];
backgroundFramesPath.forEach((path) => {
    const frameImage = new Image();
    frameImage.src = path;
    backgroundFrames.push(frameImage);
});
const buttonWidth = 150;
const buttonHeight = 50;
const buttonX = canvas.width / 2 - buttonWidth / 2;
const buttonY = canvas.height / 2 - buttonHeight / 2;
const imageWidth = 300;
const imageHeight = 600;
const imageX = canvas.width / 2 - imageWidth / 2;
const imageY = canvas.height / 2 - imageHeight / 2;
const image = new Image();
image.src = "./assets/images/sprites/cristiano-ronaldo.png";
const suiii = new Audio("./assets/sounds/SUIII.mp3");
let suiiiPlayed = false;
const backgroundMusic = new Audio("./assets/music/starwars.mp3");
canvas.addEventListener("click", (event) => {
    if (gameState === GameStates.START_MENU) {
        const rect = canvas.getBoundingClientRect();
        const clickX = event.clientX - rect.left;
        const clickY = event.clientY - rect.top;
        if (
            clickX >= buttonX &&
            clickX <= buttonX + buttonWidth &&
            clickY >= buttonY &&
            clickY <= buttonY + buttonHeight
        ) {
            gameState = GameStates.PLAYING;
        }
    }
});
document.addEventListener("keydown", (event) => {
    keys[event.code] = true;
});
document.addEventListener("keyup", (event) => {
    keys[event.code] = false;
});
function gameLoop() {
    backgroundMusic.play();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(backgroundFrames[currentFrameIndex], 0, 0, frameWidth, frameHeight);
    if (gameState === GameStates.START_MENU || gameState === GameStates.PLAYING) {
        const currentFrameIndex = Math.floor(Date.now() / 100) % backgroundFrames.length;
        ctx.drawImage(backgroundFrames[currentFrameIndex], 0, 0, canvas.width, canvas.height);
    }
    if (gameState === GameStates.START_MENU) {
        ctx.drawImage(image, imageX, imageY, imageWidth, imageHeight);
        ctx.fillStyle = "skyblue";
        ctx.fillRect(buttonX, buttonY, buttonWidth, buttonHeight);
        ctx.fillStyle = "black";
        ctx.font = "30px Algerian";
        ctx.fillText("Start", buttonX + 30, buttonY + 35);
    }
    if (gameState === GameStates.PLAYING) {
        player.update();
        player.render(ctx);
        player.bullets.forEach((bullet, index) => {
            bullet.update();
            bullet.render(ctx);
            if (bullet.y < -bullet.height) {
                player.bullets.splice(index, 1);
            }
        });
    }
    frameCount++;
    currentFrameIndex++;
    if (currentFrameIndex >= backgroundFrames.length) {
        currentFrameIndex = 0;
    }
    requestAnimationFrame(gameLoop);
}
suiii.play();
gameLoop();
