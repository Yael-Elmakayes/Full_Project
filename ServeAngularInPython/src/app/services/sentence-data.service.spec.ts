import { TestBed } from '@angular/core/testing';

import { SentenceDataService } from './sentence-data.service';

describe('SentenceDataService', () => {
  let service: SentenceDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SentenceDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
