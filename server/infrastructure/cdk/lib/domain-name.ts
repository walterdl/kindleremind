import { Construct } from "constructs";

import {
  Certificate,
  CertificateValidation,
  ICertificate,
} from "aws-cdk-lib/aws-certificatemanager";
import { HostedZone, IHostedZone } from "aws-cdk-lib/aws-route53";

export class KrDomainName extends Construct {
  readonly rootDomainName: string;
  readonly apiSubdomain = "kindleremind-api";
  readonly apiCertificate: ICertificate;
  readonly hostedZone: IHostedZone;

  constructor(scope: Construct, id: string, props: Props) {
    super(scope, id);

    this.rootDomainName = props.rootDomainName;
    this.hostedZone = HostedZone.fromHostedZoneAttributes(this, "HostedZone", {
      hostedZoneId: props.hostedZoneId,
      zoneName: this.rootDomainName,
    });

    this.apiCertificate = new Certificate(this, "Certificate", {
      domainName: this.getDomainName(this.apiSubdomain),
      validation: CertificateValidation.fromDns(this.hostedZone),
    });
  }

  getDomainName(subdomain: string) {
    return `${subdomain}.${this.rootDomainName}`;
  }
}

interface Props {
  rootDomainName: string;
  hostedZoneId: string;
}
