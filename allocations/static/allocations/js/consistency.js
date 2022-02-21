$(document).ready(function () {
    $('.items1').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items1');
            var i_clicked = -1;

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A' && radio === clickedRadio) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'B' && i_clicked != (i-1)) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    i_clicked = i;
                    continue;
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items2').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items2');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A' && radio === clickedRadio) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'B' && i_clicked != (i-1)) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    i_clicked = i;
                    continue;
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items3').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items3');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A' && radio === clickedRadio) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'B' && i_clicked != (i-1)) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    i_clicked = i;
                    continue;
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.slider').click(
        function (event) {
            var slider_id = event.target.id;
            var parent_slider = document.getElementById(slider_id).parentElement.parentElement;
            var childs = parent_slider.children;

            var dinero_pa = childs[0].firstElementChild;
            var slider_value = childs[1].firstElementChild.value;
            var dinero_pb = childs[2].firstElementChild;

            dinero_pa.innerHTML = "$ "+numberWithPoints(slider_value);
            dinero_pb.innerHTML = "$ "+numberWithPoints(600000-slider_value);
        }
    );
});

function numberWithPoints(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
