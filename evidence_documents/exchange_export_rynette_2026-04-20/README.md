# Exchange Export Reconstruction

The original `exchange-eml-export-rynette@regima.zone.tar.gz` archive exceeded GitHub's single-file size limit. It is therefore preserved here as split parts.

## Files

- `exchange-eml-export-rynette@regima.zone.tar.gz.part-000`
- `exchange-eml-export-rynette@regima.zone.tar.gz.part-001`
- `export-summary.json`
- `mailbox.json`

## Reassembly

Run the following command in this directory:

```bash
cat exchange-eml-export-rynette@regima.zone.tar.gz.part-* > exchange-eml-export-rynette@regima.zone.tar.gz
```

You can then inspect the archive with:

```bash
tar -tzf exchange-eml-export-rynette@regima.zone.tar.gz | less
```
