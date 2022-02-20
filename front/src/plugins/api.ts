import axios from 'axios'
import { useUserStore } from '@/stores/user'


const rootUrl = "https://tiragecadeaux.com/api/";

async function apiPost(path:string, data:object): Promise<object> {
  const store = useUserStore()
  const loggedIn = store.loggedIn

  console.log("Access : ", store.accessToken)

  let headers = {
    Authorization: '',
    "Content-Type": "application/json"
  }

  if (loggedIn) {
    headers.Authorization = "Bearer " + store.accessToken
  }

  const res = await axios.post(rootUrl + path, data, {
    headers
  });
  return res.data
}

export { rootUrl, apiPost }
