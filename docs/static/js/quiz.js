(function () {
    var form = document.getElementById('quizForm');
    if (!form) {
        return;
    }
    var questions = form.querySelectorAll('fieldset.quiz-q');
    var result = document.getElementById('quizResult');

    function checkQuiz() {
        var score = 0;
        var answered = 0;
        questions.forEach(function (question) {
            var answer = Number(question.getAttribute('data-answer'));
            var checked = question.querySelector('input[type="radio"]:checked');
            question.classList.remove('correct', 'wrong');
            if (!checked) {
                return;
            }
            answered += 1;
            var selected = Number(checked.value);
            if (selected === answer) {
                score += 1;
                question.classList.add('correct');
            } else {
                question.classList.add('wrong');
            }
        });
        var text = 'Puntaje: ' + score + '/' + questions.length;
        if (answered < questions.length) {
            text += ' (faltan preguntas)';
        }
        if (result) {
            result.textContent = text;
        }
    }

    function resetQuiz() {
        form.reset();
        questions.forEach(function (question) {
            question.classList.remove('correct', 'wrong');
        });
        if (result) {
            result.textContent = '';
        }
    }

    var checkButton = document.getElementById('checkQuiz');
    var resetButton = document.getElementById('resetQuiz');
    if (checkButton) {
        checkButton.addEventListener('click', checkQuiz);
    }
    if (resetButton) {
        resetButton.addEventListener('click', resetQuiz);
    }
})();
