import { MovieService } from './../movie.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-newmovie',
  templateUrl: './newmovie.component.html',
  styleUrls: ['./newmovie.component.css']
})
export class NewmovieComponent implements OnInit {

  constructor(private movie:MovieService) { }

  ngOnInit(): void {
  }

  saveMovie(e){
    this.movie.saveMovie(e.value).subscribe((res)=>{
      console.log(res);
    })
  }

}
