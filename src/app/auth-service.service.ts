import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, of } from 'rxjs'
import { map } from 'rxjs/operators'
import { Router } from '@angular/router';

export interface idToken{
  id: string;
}


@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  constructor(private http: HttpClient) { }


  public postTwitterID(user: idToken): Observable<any>{
    const base = this.http.post('http://localhost:5000/twitterID', user)
    const request = base.pipe(
      map((data: any) => {
        return data
      })
    )
    return request
  }

}
