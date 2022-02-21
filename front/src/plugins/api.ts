import axios from 'axios'
import { useUserStore } from '@/stores/user'

const rootUrl = "https://tiragecadeaux.com/api/";

function getHeaders() {
  const store = useUserStore()
  // @ts-ignore
  const loggedIn = store.loggedIn

  let headers = {
    Authorization: '',
    "Content-Type": "application/json"
  }

  if (loggedIn) {
    // @ts-ignore
    headers.Authorization = "Bearer " + store.accessToken
  }
  return headers;
}

async function apiPost(path:string, data:object): Promise<object> {
  const res = await axios.post(rootUrl + path, data, {
    headers: getHeaders()
  });
  return res.data
}

async function apiGet(path:string): Promise<object> {
  const res = await axios.get(rootUrl + path, {
    headers: getHeaders()
  });
  return res.data
}

export { rootUrl, apiPost, apiGet }
