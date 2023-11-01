function translate () {
  const lang = $('INPUT#language_code').val();
  $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data) {
    $('#hello').html(data.hello);
  });
}

$(document).ready(() => {
  $('INPUT#btn_translate').click(translate);

  $('INPUT#language_code').on('keydown', function (event) {
    if (event.key === 'Enter') {
      translate();
    }
  });
});
