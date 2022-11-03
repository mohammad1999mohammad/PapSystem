export default function ({ store, redirect, route }) {

    // we cant use exit() commit because store not load yet (maybe)
    // if (localStorage.getItem('login') === null) { localStorage.setItem('login', 'No') }

    if (localStorage.getItem('login') === null) {
        store.commit('exit')
    }

    if (localStorage.getItem('login') !== null) {
        store.commit('assign')
    }

    if ((store.state.login === 'No') && (route.fullPath !== '/login')) {
        return redirect('/login')
    }

    if ((store.state.login === 'Yes') && (route.fullPath === '/login')) {
        return redirect('/prediction')
    }

}