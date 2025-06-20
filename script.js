let secretNumber;
let maxNumber;
let attemptsLeft;

function startGame(max, attempts) {
    maxNumber = max;
    attemptsLeft = attempts;
    secretNumber = Math.floor(Math.random() * maxNumber) + 1;

    document.getElementById('menu').style.display = 'none';
    document.getElementById('game').style.display = 'block';
    document.getElementById('level-info').innerText = `🎯 Guess the number between 1 and ${maxNumber}`;
    document.getElementById('attempts-info').innerText = `Attempts Left: ${attemptsLeft}`;
    document.getElementById('feedback').innerText = '';
    document.getElementById('user-guess').value = '';
}

function checkGuess() {
    let guess = parseInt(document.getElementById('user-guess').value);

    if (guess === secretNumber) {
        document.getElementById('feedback').innerText = "🎉 Correct! You won!";
    } else if (guess < secretNumber) {
        document.getElementById('feedback').innerText = "📉 Too low! Try again.";
        attemptsLeft--;
    } else {
        document.getElementById('feedback').innerText = "📈 Too high! Try again.";
        attemptsLeft--;
    }

    document.getElementById('attempts-info').innerText = `Attempts Left: ${attemptsLeft}`;

    if (attemptsLeft === 0 && guess !== secretNumber) {
        document.getElementById('feedback').innerText = `❌ Out of attempts! The number was ${secretNumber}.`;
    }
}

function resetGame() {
    document.getElementById('menu').style.display = 'block';
    document.getElementById('game').style.display = 'none';
}



