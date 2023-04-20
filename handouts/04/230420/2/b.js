document.querySelector("#log").onclick = function() {
  let eventListener = document.createElement('eventListener')
  eventListener.setAttribute('h4', '버튼을 클릭하였습니다 !')
  document.body.append(eventListener)
};