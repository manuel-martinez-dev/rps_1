// Game logic
document.querySelectorAll('.move-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const move = btn.dataset.move;
        fetch('/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ move })
        })
        .then(r => r.json())
        .then(data => {
            const area = document.getElementById('result-area');
            if (data.result === 'win') {
                area.textContent = `You played ${data.player_move}, JOHNNY5 played ${data.ai_move} — YOU WIN!`;
                area.style.color = '#4caf50';
            } else if (data.result === 'lose') {
                area.textContent = `You played ${data.player_move}, JOHNNY5 played ${data.ai_move} — JOHNNY5 WINS!`;
                area.style.color = '#e94560';
            } else {
                area.textContent = `You played ${data.player_move}, JOHNNY5 played ${data.ai_move} — DRAW!`;
                area.style.color = '#ffeb3b';
            }
            document.getElementById('score-player').textContent = data.score_player;
            document.getElementById('score-ai').textContent = data.score_ai;
            document.getElementById('round').textContent = data.round;

            if (data.game_over) {
                document.querySelectorAll('.move-btn').forEach(b => b.disabled = true);
                area.innerHTML += `<br><strong>${data.final_result}</strong> <a href="/">Play again</a>`;
            }
        });
    });
});
