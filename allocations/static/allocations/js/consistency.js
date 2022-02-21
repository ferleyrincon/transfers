$(document).ready(function () {
    $('.items1').change(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items1');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    continue;
                }

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }
                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items2').change(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items2');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    continue;
                }

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }
                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items3').change(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items3');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    continue;
                }

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }
                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }
            }
        }
    );
});
