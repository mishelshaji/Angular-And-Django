import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(private http:HttpClient) { }

  getMovieList(){
    return this.http.get("http://127.0.0.1:8000/api/");
  }

  saveMovie(data){
    return this.http.post("http://127.0.0.1:8000/api/create/", data);
  }
}
