export default function (ctx) {

  // we cant use exit() commit because store not load yet (maybe)
  // if (localStorage.getItem('login') === null) {
  //   store.commit('exit')
  // }

  if (ctx.route.fullPath === '/')
    ctx.redirect('/prediction')

}