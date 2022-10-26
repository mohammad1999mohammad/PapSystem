export default function ({ store, redirect }) {

    if (store.state.login === 'No') {
        return redirect('/login')
    }

}