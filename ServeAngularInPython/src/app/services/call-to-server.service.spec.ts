import { TestBed } from '@angular/core/testing';

import { CallToServerService } from './call-to-server.service';

describe('CallToServerService', () => {
  let service: CallToServerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CallToServerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
