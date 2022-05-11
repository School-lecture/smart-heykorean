// project
	// ui-picker.html
		$('#doc_datepicker_example_1').datepicker();

		$('#doc_datepicker_example_2').datepicker({
			format: "dd-mmm-yyyy",
			selectMonths: true,
			selectYears: 30
		});

	// ui-progress.html
		$('.finish-loading').on('click', function(e) {
			e.stopPropagation();
			$($(this).attr('data-target')).addClass('el-loading-done');
		});

		$('#doc_el_loading_example_wrap .tile-active-show').each(function (index) {
			var $this = $(this),
			    timer;

			$this.on('hide.bs.tile', function(e) {
				clearTimeout(timer);
			});

			$this.on('show.bs.tile', function(e) {
				if (!$('.el-loading', $this).hasClass('el-loading-done')) {
					timer = setTimeout(function() {
						$('.el-loading', $this).addClass('el-loading-done');
						$this.prepend('<div class="tile-sub"><p>Additional information<br><small>Aliquam in pharetra leo. In congue, massa sed elementum dictum, justo quam efficitur risus, in posuere mi orci ultrices diam.</small></p></div>');
					}, 6000);
				};
			});
		});

	// ui-snackbar.html
		var snackbarText = 1;

		$('#doc_snackbar_toggle_1').on('click', function () {
			$('body').snackbar({
				content: 'Simple snackbar ' + snackbarText + ' with some text',
				show: function () {
					snackbarText++;
				}
			});
		});

		$('#doc_snackbar_toggle_2').on('click', function () {
			$('body').snackbar({
				content: '<a data-dismiss="snackbar">Dismiss</a><div class="snackbar-text">Simple snackbar ' + snackbarText + ' with some text and a simple <a href="javascript:void(0)">link</a>.</div>',
				show: function () {
					snackbarText++;
				}
			});
		});


// modal

function modal(id) {
	var zIndex = 9999;
	var modal = document.getElementById(id);
	// 모달 div 뒤에 레이어         
	var bg = document.createElement('div');
	bg.setStyle({
		position: 'fixed',
		zIndex: zIndex,
		left: '0px',
		top: '0px',
		width: '100%',
		height: '100%',
		overflow: 'auto',
		// 레이어 색은 여기서 바꾸면 됨
		backgroundColor: 'rgba(0,0,0,0.4)'
	});
	document
		.body
		.append(bg);

	// 닫기 버튼 처리, 레이어와 모달 div 지우기
	modal
		.querySelector('.modal_close_btn')
		.addEventListener('click', function () {
			bg.remove();
			modal.style.display = 'none';
		});

	modal.setStyle({
		position: 'fixed', display: 'block', boxShadow: '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)',

		// 시꺼먼 레이어 보다 한칸 위에 보이기
		zIndex: zIndex + 1,

		// div center 정렬
		top: '50%',
		left: '50%',
		transform: 'translate(-50%, -50%)',
		msTransform: 'translate(-50%, -50%)',
		webkitTransform: 'translate(-50%, -50%)'
	});
}

// Element 에 style 한번에 오브젝트로 설정하는 함수 추가
Element.prototype.setStyle = function (styles) {
	for (var k in styles) 
		this.style[k] = styles[k];
	return this;
};

document
	.getElementById('popup_open_btn')
	.addEventListener('click', function () {
		// 모달창 띄우기
		modal('my_modal');
	});

// checkbox 중복방지
function checkOnlyOne(element) {
	const checkboxes = document.getElementsByName("song");
	checkboxes.forEach((cb) => {
		cb.checked = false;
	})
	element.checked = true;
}      
