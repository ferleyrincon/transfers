$(document).ready(function () {
    $('.x-items').change(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.x-items');

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
    $('.y-items').change(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.y-items');

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